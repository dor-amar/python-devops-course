"""BeautifulSoup web scraping module."""

import os
import time
from typing import Any, Dict, List, Optional, Union
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn


# Initialize Rich console
console = Console()


class BeautifulSoupScraper:
    """Manager for BeautifulSoup web scraping."""

    def __init__(
        self,
        base_url: str,
        user_agent: Optional[str] = None,
        timeout: int = 10,
        max_retries: int = 3,
        delay: float = 1.0
    ):
        """Initialize the scraper.

        Args:
            base_url: Base URL for scraping
            user_agent: Custom user agent (optional)
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
            delay: Delay between requests in seconds
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': user_agent or UserAgent().random
        })
        self.timeout = timeout
        self.max_retries = max_retries
        self.delay = delay
        self.soup: Optional[BeautifulSoup] = None

    def get_page(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None
    ) -> BeautifulSoup:
        """Get and parse a web page.

        Args:
            url: URL to fetch
            params: Query parameters (optional)

        Returns:
            BeautifulSoup: Parsed HTML content
        """
        full_url = urljoin(self.base_url, url)
        retries = 0

        while retries < self.max_retries:
            try:
                response = self.session.get(
                    full_url,
                    params=params,
                    timeout=self.timeout
                )
                response.raise_for_status()
                self.soup = BeautifulSoup(response.text, 'lxml')
                time.sleep(self.delay)
                return self.soup

            except requests.RequestException as e:
                retries += 1
                if retries == self.max_retries:
                    console.print(f"[red]Error fetching {full_url}: {e}[/]")
                    raise
                time.sleep(self.delay * retries)

    def find_elements(
        self,
        selector: str,
        by: str = 'css'
    ) -> List[BeautifulSoup]:
        """Find elements using CSS or XPath selector.

        Args:
            selector: CSS or XPath selector
            by: Selector type ('css' or 'xpath')

        Returns:
            List[BeautifulSoup]: List of matching elements
        """
        if not self.soup:
            raise RuntimeError("No page loaded")

        if by == 'css':
            return self.soup.select(selector)
        elif by == 'xpath':
            return self.soup.find_all(xpath=selector)
        else:
            raise ValueError("Invalid selector type")

    def extract_text(
        self,
        selector: str,
        by: str = 'css',
        strip: bool = True
    ) -> Optional[str]:
        """Extract text from an element.

        Args:
            selector: CSS or XPath selector
            by: Selector type ('css' or 'xpath')
            strip: Whether to strip whitespace

        Returns:
            Optional[str]: Extracted text
        """
        elements = self.find_elements(selector, by)
        if not elements:
            return None

        text = elements[0].get_text()
        return text.strip() if strip else text

    def extract_links(
        self,
        selector: str = 'a',
        by: str = 'css',
        absolute: bool = True
    ) -> List[Dict[str, str]]:
        """Extract links from the page.

        Args:
            selector: CSS or XPath selector
            by: Selector type ('css' or 'xpath')
            absolute: Whether to convert to absolute URLs

        Returns:
            List[Dict[str, str]]: List of link dictionaries
        """
        links = []
        elements = self.find_elements(selector, by)

        for element in elements:
            href = element.get('href')
            if not href:
                continue

            if absolute:
                href = urljoin(self.base_url, href)

            links.append({
                'text': element.get_text(strip=True),
                'url': href
            })

        return links

    def extract_table(
        self,
        selector: str,
        by: str = 'css',
        headers: bool = True
    ) -> List[Dict[str, str]]:
        """Extract data from a table.

        Args:
            selector: CSS or XPath selector
            by: Selector type ('css' or 'xpath')
            headers: Whether to use first row as headers

        Returns:
            List[Dict[str, str]]: List of row dictionaries
        """
        table = self.find_elements(selector, by)[0]
        rows = table.find_all('tr')
        data = []

        if headers and rows:
            headers = [th.get_text(strip=True) for th in rows[0].find_all(['th', 'td'])]
            rows = rows[1:]

        for row in rows:
            cells = row.find_all(['td', 'th'])
            row_data = {}
            
            for i, cell in enumerate(cells):
                key = headers[i] if headers else f'column_{i}'
                row_data[key] = cell.get_text(strip=True)

            data.append(row_data)

        return data

    def submit_form(
        self,
        selector: str,
        data: Dict[str, str],
        by: str = 'css'
    ) -> BeautifulSoup:
        """Submit a form on the page.

        Args:
            selector: CSS or XPath selector
            data: Form data to submit
            by: Selector type ('css' or 'xpath')

        Returns:
            BeautifulSoup: Parsed response
        """
        if not self.soup:
            raise RuntimeError("No page loaded")

        form = self.find_elements(selector, by)[0]
        action = form.get('action', '')
        method = form.get('method', 'get').upper()
        url = urljoin(self.base_url, action)

        try:
            if method == 'GET':
                response = self.session.get(url, params=data, timeout=self.timeout)
            else:
                response = self.session.post(url, data=data, timeout=self.timeout)

            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, 'lxml')
            time.sleep(self.delay)
            return self.soup

        except requests.RequestException as e:
            console.print(f"[red]Error submitting form: {e}[/]")
            raise

    def save_screenshot(self, filename: str) -> None:
        """Save the current page as HTML.

        Args:
            filename: Output filename
        """
        if not self.soup:
            raise RuntimeError("No page loaded")

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(self.soup))
        console.print(f"[green]Saved page to {filename}[/]")

    def display_data(self, data: List[Dict[str, str]], title: str = "Scraped Data") -> None:
        """Display scraped data in a formatted table.

        Args:
            data: List of data dictionaries
            title: Table title
        """
        if not data:
            console.print("[yellow]No data to display[/]")
            return

        table = Table(title=title)
        for key in data[0].keys():
            table.add_column(key, style="cyan")

        for row in data:
            table.add_row(*[str(row[key]) for key in data[0].keys()])

        console.print(table)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize scraper
        scraper = BeautifulSoupScraper(
            base_url="https://example.com",
            delay=2.0
        )

        # Get and parse a page
        console.print("\n[bold]Fetching page...[/]")
        scraper.get_page("/")

        # Extract text
        console.print("\n[bold]Extracting text...[/]")
        title = scraper.extract_text('h1')
        console.print(f"Page title: {title}")

        # Extract links
        console.print("\n[bold]Extracting links...[/]")
        links = scraper.extract_links()
        scraper.display_data(links, "Page Links")

        # Extract table data
        console.print("\n[bold]Extracting table data...[/]")
        table_data = scraper.extract_table('table')
        scraper.display_data(table_data, "Table Data")

        # Submit a form
        console.print("\n[bold]Submitting form...[/]")
        form_data = {
            'username': 'test_user',
            'password': 'test_pass'
        }
        scraper.submit_form('form', form_data)

        # Save page
        scraper.save_screenshot('page.html')

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 
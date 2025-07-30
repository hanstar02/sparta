import asyncio
from typing import List

from pydoll.browser import Chrome


async def fetch_reviews(product_url: str, pages: int = 1) -> List[str]:
    """Fetch reviews from a Coupang product page using Pydoll.

    Parameters
    ----------
    product_url : str
        URL of the Coupang product.
    pages : int, optional
        Number of review pages to fetch, by default 1.

    Returns
    -------
    List[str]
        Collected review texts.
    """
    reviews: List[str] = []
    async with Chrome() as browser:
        tab = await browser.start()
        await tab.go_to(product_url)

        # Click the review tab if present
        try:
            review_tab = await tab.query('a[href*="review"]', timeout=5)
            if review_tab:
                await review_tab.click()
        except Exception:
            # Tab might already be active
            pass

        for page in range(1, pages + 1):
            # Wait for review articles
            articles = await tab.query(
                'article.sdp-review__article__list__review',
                find_all=True,
                timeout=5,
            )
            for article in articles:
                try:
                    content = await article.find(
                        class_name='sdp-review__article__list__review__content',
                    )
                    text = await content.text
                    reviews.append(text.strip())
                except Exception:
                    continue

            # Go to next review page
            if page < pages:
                try:
                    next_button = await tab.query(
                        'button.sdp-review__article__page__next',
                        timeout=5,
                    )
                    if next_button:
                        await next_button.click()
                        await asyncio.sleep(1)
                except Exception:
                    break

    return reviews


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Scrape Coupang product reviews")
    parser.add_argument("url", help="Coupang product URL")
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of review pages to scrape",
    )
    args = parser.parse_args()

    result = asyncio.run(fetch_reviews(args.url, args.pages))
    for idx, review in enumerate(result, 1):
        print(f"{idx}. {review}")


if __name__ == "__main__":
    main()

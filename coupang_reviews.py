import asyncio
from pydoll.browser import Chrome

async def fetch_reviews(product_url: str, pages: int = 1):
    reviews = []
    async with Chrome() as browser:
        tab = await browser.start()
        await tab.go_to(product_url)

        # 리뷰 탭 클릭
        try:
            review_tab = await tab.query('a[href*="review"]', timeout=5)
            if review_tab:
                await review_tab.click()
        except Exception:
            pass

        # 페이지별 리뷰 추출
        for page in range(1, pages + 1):
            articles = await tab.query('article.sdp-review__article__list__review', find_all=True)
            for article in articles:
                try:
                    content = await article.find(class_name='sdp-review__article__list__review__content')
                    text = await content.text
                    reviews.append(text.strip())
                except Exception:
                    continue

            # 다음 페이지로 이동
            if page < pages:
                next_button = await tab.query('button.sdp-review__article__page__next', timeout=5)
                if next_button:
                    await next_button.click()
                    await asyncio.sleep(1)

    return reviews

# 실행
async def main():
    product_url = "https://www.coupang.com/vp/products/1234567890"  # 쿠팡 상품 URL
    reviews = await fetch_reviews(product_url, pages=3)
    
    for idx, review in enumerate(reviews, 1):
        print(f"{idx}. {review}")

if __name__ == "__main__":
    asyncio.run(main())

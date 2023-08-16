import os
import ssl
import feedparser
import hashlib

from cufeed.models import Feeds


class FeedService:
    hash_salt = os.getenv("HASH_SALT")

    def collect_feeds(self, vendor, keyword):

        try:
            if vendor == 'google':
                url = 'https://news.google.com/rss/search?q=' + keyword + '+when:1d&hl=ko&gl=KR&ceid=KR:ko'
            else:
                raise ValueError

            ssl._create_default_https_context = ssl._create_unverified_context
            rss = feedparser.parse(url)

            for item in rss.entries:
                title = item.title
                link = item.link
                link_hash = hashlib.md5((title + link + self.hash_salt).encode("utf-8")).hexdigest()

                # 뉴스 제목이 같은 건 스킵한다.
                valid_count = Feeds.objects.filter(title=title).count()

                # 같은 link_hash가 존재해도 등록하지 않고 스킵한다.
                valid_count = valid_count + Feeds.objects.filter(link_hash=link_hash).count()

                if valid_count > 0:
                    print("Already content:", title)
                else:
                    # TODO: keyword는 id로 변경해야함.
                    record = Feeds(title=title, link=link, link_hash=link_hash, vendor=vendor, keyword=keyword)
                    record.save()

                print("title:", title, ", link:", link)

            return True
        except ValueError:
            raise Exception("bad request")

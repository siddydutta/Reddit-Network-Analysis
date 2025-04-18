from dataclasses import dataclass


REDDIT_BASE_URL = 'https://reddit.com'
SUBMISSION_ID_PREFIX = 't3_'


@dataclass
class Submission:
    id_: str
    subreddit: str
    title: str
    selftext: str
    url: str
    author: str
    ups: int
    score: int
    permalink: str
    created_utc: int
    num_comments: int

    @property
    def link(self) -> str:
        return REDDIT_BASE_URL + self.permalink

def json_to_submission(data: dict) -> Submission:
    return Submission(
        id_=SUBMISSION_ID_PREFIX + data['id'],
        subreddit=data['subreddit'],
        title=data['title'],
        selftext=data['selftext'],
        url=data['url'],
        author=data['author'],
        ups=data['ups'],
        score=data['score'],
        permalink=data['permalink'],
        created_utc=int(data['created_utc']),
        num_comments=data['num_comments'],
    )

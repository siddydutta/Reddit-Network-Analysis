from dataclasses import dataclass


REDDIT_BASE_URL = 'https://reddit.com'
COMMENT_ID_PREFIX = 't1_'


@dataclass
class Comment:
    id_: str
    parent_id: str
    submission_id: str
    body: str
    author: str
    created_utc: int
    ups: int
    score: int

    def get_link(self, subreddit: str = 'InvestmentClub') -> str:
        return f'{REDDIT_BASE_URL}/r/{subreddit}/comments/{self.submission_id[3:]}/comment/{self.id_[3:]}/'

def json_to_comment(data: dict) -> Comment:
    return Comment(
        id_=COMMENT_ID_PREFIX + data['id'],
        parent_id=data['parent_id'],
        submission_id=data['link_id'],
        body=data['body'],
        author=data['author'],
        created_utc=int(data['created_utc']),
        ups=data['ups'],
        score=data['score'],
    )

from collections import deque
from .comment import Comment
from .submission import Submission


class CommentNode:
    def __init__(self, comment: Comment, depth: int = 0):
        self.comment = comment
        self.children = []
        self.depth = depth


class Post:
    def __init__(self, submission: Submission):
        self.submission = submission
        self.comments: list[CommentNode] = []

    @staticmethod
    def construct_post(submission: Submission, comments: dict[str, Comment]) -> 'Post':
        post = Post(submission)
        curr_level = {comment.id_: CommentNode(comment)
                      for comment in comments.values()
                      if comment.parent_id == comment.submission_id}
        post.comments = list(curr_level.values())
        for comment_id in curr_level:
            comments.pop(comment_id)
        while comments:
            next_level = {}
            for comment in comments.values():
                parent_id = comment.parent_id
                if parent_id in curr_level:
                    node = CommentNode(comment)
                    node.depth = curr_level[parent_id].depth + 1
                    curr_level[parent_id].children.append(node)
                    next_level[comment.id_] = node
            curr_level = next_level
            for comment_id in curr_level:
                comments.pop(comment_id)
            if not curr_level:
                break
        return post

    def comment_stats(self) -> tuple[int, int]:
        num_comments = 0
        max_depth = 0
        queue = deque(self.comments)
        while queue:
            node = queue.popleft()
            num_comments += 1
            max_depth = max(max_depth, node.depth)
            queue.extend(node.children)
        return num_comments, max_depth

    def get_all_comments(self) -> list[Comment]:
        comments = []
        queue = deque(self.comments)
        while queue:
            node = queue.popleft()
            comments.append(node.comment)
            queue.extend(node.children)
        return comments

class NewsModel:
    def __init__(self, id, authors, status, classification, title, content, fact, references, source_issue, source_link, picture1, picture2, tanggal, tags, conclusion, claim_review=None, media=None):
        self.id = id
        self.authors = authors
        self.status = status
        self.classification = classification
        self.title = title
        self.content = content
        self.fact = fact
        self.references = references
        self.source_issue = source_issue
        self.source_link = source_link
        self.picture1 = picture1
        self.picture2 = picture2
        self.tanggal = tanggal
        self.tags = tags
        self.conclusion = conclusion
        self.claim_review = claim_review or []
        self.media = media or []

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id'),
            authors=data.get('authors'),
            status=data.get('status'),
            classification=data.get('classification'),
            title=data.get('title'),
            content=data.get('content'),
            fact=data.get('fact'),
            references=data.get('references'),
            source_issue=data.get('source_issue'),
            source_link=data.get('source_link'),
            picture1=data.get('picture1'),
            picture2=data.get('picture2'),
            tanggal=data.get('tanggal'),
            tags=data.get('tags'),
            conclusion=data.get('conclusion'),
            claim_review=data.get('claim_review', []),
            media=data.get('media', [])
        )

    def __str__(self):
        return f"News(id={self.id}, title={self.title}, status={self.status})"

    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            'id': self.id,
            'authors': self.authors,
            'status': self.status,
            'classification': self.classification,
            'title': self.title,
            'content': self.content,
            'fact': self.fact,
            'references': self.references,
            'source_issue': self.source_issue,
            'source_link': self.source_link,
            'picture1': self.picture1,
            'picture2': self.picture2,
            'tanggal': self.tanggal,
            'tags': self.tags,
            'conclusion': self.conclusion,
            'claim_review': self.claim_review,
            'media': self.media
        }

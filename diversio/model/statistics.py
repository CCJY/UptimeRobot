from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Statistics:
    pass

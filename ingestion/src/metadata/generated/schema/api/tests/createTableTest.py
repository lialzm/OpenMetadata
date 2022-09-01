# generated by datamodel-codegen:
#   filename:  schema/api/tests/createTableTest.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...tests import basic as basic_1
from ...tests import tableTest
from ...type import basic, entityReference


class CreateTableTestRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    description: Optional[basic.Markdown] = Field(
        None, description='Description of the testcase.'
    )
    testCase: tableTest.TableTestCase
    executionFrequency: Optional[basic_1.TestCaseExecutionFrequency] = None
    result: Optional[basic_1.TestCaseResult] = None
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this Pipeline.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
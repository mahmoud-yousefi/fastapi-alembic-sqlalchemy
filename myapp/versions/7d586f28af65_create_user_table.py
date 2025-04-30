"""Create User Table

Revision ID: 7d586f28af65
Revises: 
Create Date: 2025-04-29 01:30:08.528828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d586f28af65'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "employee",
        # sa col, id name string 50, current bool default true
        sa
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass

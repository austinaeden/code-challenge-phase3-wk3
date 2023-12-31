"""created tables

Revision ID: 254706a5fa26
Revises: 8052d4c3a07e
Create Date: 2023-09-05 15:43:20.889815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '254706a5fa26'
down_revision = '8052d4c3a07e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('star_rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'star_rating')
    # ### end Alembic commands ###

"""created tables

Revision ID: b627d79120d8
Revises: a95e570a81b0
Create Date: 2023-09-05 09:05:54.397786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b627d79120d8'
down_revision = 'a95e570a81b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('cus_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cus_id')
    )
    op.create_table('restaurant',
    sa.Column('res_id', sa.Integer(), nullable=False),
    sa.Column('res_name', sa.String(), nullable=True),
    sa.Column('res_price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('res_id')
    )
    op.create_table('review',
    sa.Column('rev_id', sa.Integer(), nullable=False),
    sa.Column('cus_id', sa.Integer(), nullable=True),
    sa.Column('res_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cus_id'], ['customer.cus_id'], ),
    sa.ForeignKeyConstraint(['res_id'], ['restaurant.res_id'], ),
    sa.PrimaryKeyConstraint('rev_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('restaurant')
    op.drop_table('customer')
    # ### end Alembic commands ###

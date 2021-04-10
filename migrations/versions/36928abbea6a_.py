"""empty message

Revision ID: 36928abbea6a
Revises: 7b29211730a6
Create Date: 2021-04-10 01:41:36.763561

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '36928abbea6a'
down_revision = '7b29211730a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('title2', sa.String(length=100), nullable=False))
    op.drop_column('films', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('title', mysql.VARCHAR(length=28), nullable=False))
    op.drop_column('films', 'title2')
    # ### end Alembic commands ###

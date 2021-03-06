"""empty message

Revision ID: e76d6203194c
Revises: 812bab70cef5
Create Date: 2020-06-03 10:50:08.524547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e76d6203194c'
down_revision = '812bab70cef5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'text',
               existing_type=sa.VARCHAR(length=1000),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'text',
               existing_type=sa.VARCHAR(length=1000),
               nullable=True)
    # ### end Alembic commands ###

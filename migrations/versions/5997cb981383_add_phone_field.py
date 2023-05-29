"""add phone field

Revision ID: 5997cb981383
Revises: e7750e1b0009
Create Date: 2023-03-29 11:47:27.892947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5997cb981383'
down_revision = 'e7750e1b0009'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('phone')

    # ### end Alembic commands ###

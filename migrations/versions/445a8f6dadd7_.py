"""empty message

Revision ID: 445a8f6dadd7
Revises: 5cc296299cf6
Create Date: 2023-04-20 23:54:50.603073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '445a8f6dadd7'
down_revision = '5cc296299cf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('eyecolor', sa.String(length=15), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_column('eyecolor')

    # ### end Alembic commands ###

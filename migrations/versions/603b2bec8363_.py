"""empty message

Revision ID: 603b2bec8363
Revises: 
Create Date: 2021-12-08 15:51:09.114801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '603b2bec8363'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lottery_participant',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=True),
    sa.Column('choice', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('participant_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lottery_participant')
    # ### end Alembic commands ###

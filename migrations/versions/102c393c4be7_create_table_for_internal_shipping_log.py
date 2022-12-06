"""Create Table for Internal Shipping Log 

Revision ID: 102c393c4be7
Revises: c06634c072fd
Create Date: 2022-11-17 09:15:07.520234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '102c393c4be7'
down_revision = 'c06634c072fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('IntShipLogModel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tstamp', sa.Text(), nullable=True),
    sa.Column('customer', sa.Text(), nullable=True),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('productName', sa.Text(), nullable=True),
    sa.Column('qrCode', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('IntShipLogModel')
    # ### end Alembic commands ###

"""First step

Revision ID: 2e26571834ea
Revises: None
Create Date: 2013-06-30 15:07:31.746984

"""

# revision identifiers, used by Alembic.
revision = '2e26571834ea'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vendor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vendor_name', sa.String(length=80), nullable=True),
    sa.Column('contact_email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contact_email'),
    sa.UniqueConstraint('vendor_name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vendor')
    ### end Alembic commands ###

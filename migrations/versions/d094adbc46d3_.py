"""empty message

Revision ID: d094adbc46d3
Revises: 
Create Date: 2019-10-02 23:28:16.361490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd094adbc46d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('haunt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spectre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ghost_id', sa.String(length=8), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_root', sa.Boolean(), nullable=True),
    sa.Column('haunt_id', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['haunt_id'], ['haunt.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['spectre.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ghost_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spectre')
    op.drop_table('haunt')
    # ### end Alembic commands ###

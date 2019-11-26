"""Documents and Comments tables

Revision ID: 8306b848989c
Revises: a572d81a5491
Create Date: 2019-11-26 09:13:42.365390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8306b848989c'
down_revision = 'a572d81a5491'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uploaded_by', sa.Integer(), nullable=False),
    sa.Column('document_type', sa.Enum('meeting_notes', 'board_internal', name='documenttype'), nullable=True),
    sa.Column('filepath', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['uploaded_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('document', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.ForeignKeyConstraint(['document'], ['document.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('document')
    # ### end Alembic commands ###

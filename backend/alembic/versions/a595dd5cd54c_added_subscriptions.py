"""Added subscriptions

Revision ID: a595dd5cd54c
Revises: 6fcb5bee1878
Create Date: 2023-06-23 22:57:59.375444

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a595dd5cd54c'
down_revision = '6fcb5bee1878'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Subscriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('available_sessions', sa.Float(), nullable=True),
    sa.Column('visited_sessions', sa.Float(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['Clients.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['Teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('Clients_teacher_id_fkey', 'Clients', type_='foreignkey')
    op.drop_column('Clients', 'used_sessions')
    op.drop_column('Clients', 'teacher_id')
    op.drop_column('Clients', 'available_sessions')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Clients', sa.Column('available_sessions', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('Clients', sa.Column('teacher_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Clients', sa.Column('used_sessions', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.create_foreign_key('Clients_teacher_id_fkey', 'Clients', 'Teachers', ['teacher_id'], ['id'])
    op.drop_table('Subscriptions')
    # ### end Alembic commands ###

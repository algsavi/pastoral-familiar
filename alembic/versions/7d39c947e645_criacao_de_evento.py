"""criacao de evento

Revision ID: 7d39c947e645
Revises: 49860c68bb3f
Create Date: 2016-01-27 18:42:31.553000

"""

# revision identifiers, used by Alembic.
revision = '7d39c947e645'
down_revision = '49860c68bb3f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
     op.create_table(
        'evento',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('descricao', sa.VARCHAR(100), nullable=False),
        sa.Column('dt_evento', sa.Date(), nullable=False),
        sa.Column('tp_evento', sa.CHAR(1), nullable=False),
        sa.Column('id_nucleo', sa.Integer, sa.ForeignKey('nucleo.id'))
    )


def downgrade():
    op.drop_table('evento')

"""criacao de campos evento e sexo agente

Revision ID: 7f2e5ad7b3bd
Revises: a0c55e119397
Create Date: 2016-02-16 15:43:50.039000

"""

# revision identifiers, used by Alembic.
revision = '7f2e5ad7b3bd'
down_revision = 'a0c55e119397'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('agente', sa.Column('sexo', sa.CHAR(1)))
    op.add_column('evento', sa.Column('aberto_inscricao', sa.Boolean()))


def downgrade():
    op.drop_column('agente', 'sexo')
    op.drop_column('agente', 'aberto_inscricao')
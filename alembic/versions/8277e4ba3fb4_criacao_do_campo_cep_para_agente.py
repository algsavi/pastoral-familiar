"""Criacao do campo CEP para agente

Revision ID: 8277e4ba3fb4
Revises: a82d7c57405b
Create Date: 2016-01-18 14:21:41.219000

"""

# revision identifiers, used by Alembic.
revision = '8277e4ba3fb4'
down_revision = 'a82d7c57405b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('agente', sa.Column('cep', sa.VARCHAR(10), nullable=False))


def downgrade():
    op.drop_column('agente', 'cep')

"""Criacao do campo CEP para agente

Revision ID: a82d7c57405b
Revises: 4a486ac59483
Create Date: 2016-01-18 13:56:04.440000

"""

# revision identifiers, used by Alembic.
revision = 'a82d7c57405b'
down_revision = '4a486ac59483'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
     op.add_column('agente', sa.Column('cep', sa.VARCHAR(10), nullable=False))


def downgrade():
    op.drop_column('agente', 'cep')

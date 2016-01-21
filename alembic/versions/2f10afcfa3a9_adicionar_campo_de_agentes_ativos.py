"""Adicionar campo de agentes ativos

Revision ID: 2f10afcfa3a9
Revises: 7d7250c12ccf
Create Date: 2016-01-20 14:20:55.476000

"""

# revision identifiers, used by Alembic.
revision = '2f10afcfa3a9'
down_revision = '7d7250c12ccf'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('agente', sa.Column('ativo', sa.Boolean, nullable=True))


def downgrade():
    op.drop_column('agente', 'ativo')

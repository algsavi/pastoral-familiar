"""Adicionar campo para agente coordenador

Revision ID: 7d7250c12ccf
Revises: 8277e4ba3fb4
Create Date: 2016-01-19 16:05:06.468000

"""

# revision identifiers, used by Alembic.
revision = '7d7250c12ccf'
down_revision = '8277e4ba3fb4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('agente', sa.Column('coordenador_pastoral', sa.Boolean, nullable=True))


def downgrade():
    op.drop_column('agente', 'coordenador_pastoral')

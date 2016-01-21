"""criacao de campo para identificar se agente e coordenador do nucleo

Revision ID: 7b43fff73f4e
Revises: 2f10afcfa3a9
Create Date: 2016-01-20 16:53:07.021000

"""

# revision identifiers, used by Alembic.
revision = '7b43fff73f4e'
down_revision = '2f10afcfa3a9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('agente', sa.Column('coordenador_nucleo', sa.Boolean, nullable=True))


def downgrade():
    op.drop_column('agente', 'coordenador_nucleo')

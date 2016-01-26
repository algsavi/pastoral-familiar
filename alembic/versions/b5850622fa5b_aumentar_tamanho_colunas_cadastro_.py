"""aumentar tamanho colunas cadastro agentes

Revision ID: b5850622fa5b
Revises: 7b43fff73f4e
Create Date: 2016-01-26 20:43:01.723000

"""

# revision identifiers, used by Alembic.
revision = 'b5850622fa5b'
down_revision = '7b43fff73f4e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('agente', sa.Column('nome', sa.VARCHAR(65)))


def downgrade():
    op.alter_column('agente', sa.Column('nome', sa.VARCHAR(35)))

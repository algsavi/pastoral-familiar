"""aumentar tamanho colunas cadastro agentes

Revision ID: 49860c68bb3f
Revises: b5850622fa5b
Create Date: 2016-01-26 20:48:52.500000

"""

# revision identifiers, used by Alembic.
revision = '49860c68bb3f'
down_revision = 'b5850622fa5b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('ALTER TABLE agente ALTER COLUMN nome TYPE varchar(65)')
    op.execute('ALTER TABLE agente ALTER COLUMN endereco TYPE varchar(125)')


def downgrade():
    op.execute('ALTER TABLE agente ALTER COLUMN nome TYPE varchar(35)')
    op.execute('ALTER TABLE agente ALTER COLUMN endereco TYPE varchar(65)')

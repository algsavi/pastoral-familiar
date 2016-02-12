"""criar novos campos para agentes

Revision ID: d21b6b3bae03
Revises: e724c0559d33
Create Date: 2016-02-12 14:16:43.100000

"""

# revision identifiers, used by Alembic.
revision = 'd21b6b3bae03'
down_revision = 'e724c0559d33'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('ALTER TABLE agente RENAME COLUMN endereco TO rua')
    op.execute('ALTER TABLE agente ALTER COLUMN rua TYPE varchar(65)')
    op.add_column('agente', sa.Column('uf', sa.VARCHAR(2), nullable=True))
    op.add_column('agente', sa.Column('numero', sa.Integer(), nullable=True))


def downgrade():
    op.execute('ALTER TABLE agente RENAME COLUMN rua TO endereco')
    op.execute('ALTER TABLE agente ALTER COLUMN endereco TYPE varchar(125)')
    op.execute('ALTER TABLE agente DROP COLUMN uf')
    op.execute('ALTER TABLE agente DROP COLUMN numero')
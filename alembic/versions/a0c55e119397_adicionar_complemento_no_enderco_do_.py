"""adicionar complemento no enderco do agente

Revision ID: a0c55e119397
Revises: d21b6b3bae03
Create Date: 2016-02-12 15:41:44.432000

"""

# revision identifiers, used by Alembic.
revision = 'a0c55e119397'
down_revision = 'd21b6b3bae03'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('agente', sa.Column('complemento', sa.VARCHAR(30), nullable=True))


def downgrade():
    op.execute('ALTER TABLE agente DROP COLUMN complemento')

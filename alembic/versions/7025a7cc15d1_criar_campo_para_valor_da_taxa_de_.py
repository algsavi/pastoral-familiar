"""criar campo para valor da taxa de inscricao do evento

Revision ID: 7025a7cc15d1
Revises: 7d39c947e645
Create Date: 2016-01-28 15:44:33.617000

"""

# revision identifiers, used by Alembic.
revision = '7025a7cc15d1'
down_revision = '7d39c947e645'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('ALTER TABLE evento ADD COLUMN tx_inscricao DECIMAL(7, 2)')


def downgrade():
    op.execute('ALTER TABLE evento DROP COLUMN tx_inscricao')

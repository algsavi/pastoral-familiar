"""adicionar dt e local de casamento inscricao

Revision ID: 1ebad2064528
Revises: e39357dd841f
Create Date: 2016-02-24 15:58:21.349000

"""

# revision identifiers, used by Alembic.
revision = '1ebad2064528'
down_revision = 'e39357dd841f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('casal_encontrista', sa.Column('dt_casamento', sa.Date(), nullable=True))
    op.add_column('casal_encontrista', sa.Column('paroquia_casamento', sa.VARCHAR(100), nullable=True))
    op.execute('ALTER TABLE encontrista ALTER COLUMN dt_nascimento DROP NOT NULL;')


def downgrade():
    op.drop_column('casal_encontrista', 'dt_casamento')
    op.drop_column('casal_encontrista', 'paroquia_casamento')
    op.execute('ALTER TABLE encontrista ALTER COLUMN dt_nascimento SET NOT NULL;')

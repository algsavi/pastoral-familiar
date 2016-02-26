"""remover campos obrigatorios inscricao encontrista

Revision ID: 2a07a6c0c9a8
Revises: 1ebad2064528
Create Date: 2016-02-26 18:40:10.140000

"""

# revision identifiers, used by Alembic.
revision = '2a07a6c0c9a8'
down_revision = '1ebad2064528'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('ALTER TABLE encontrista ALTER COLUMN celular DROP NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN rua DROP NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN cep DROP NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN numero DROP NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN complemento DROP NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN cidade DROP NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN bairro DROP NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN uf DROP NOT NULL;')


def downgrade():
    op.execute('ALTER TABLE encontrista ALTER COLUMN celular SET NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN rua SET NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN cep SET NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN numero SET NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN complemento SET NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN cidade SET NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN bairro SET NOT NULL;')
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN uf SET NOT NULL;')

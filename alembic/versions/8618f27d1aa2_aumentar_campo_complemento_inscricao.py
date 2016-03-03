"""aumentar campo complemento inscricao

Revision ID: 8618f27d1aa2
Revises: 2a07a6c0c9a8
Create Date: 2016-03-03 15:14:09.422000

"""

# revision identifiers, used by Alembic.
revision = '8618f27d1aa2'
down_revision = '2a07a6c0c9a8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN complemento TYPE VARCHAR(30)')


def downgrade():
    op.execute('ALTER TABLE casal_encontrista ALTER COLUMN complemento TYPE VARCHAR(10)')

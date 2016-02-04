"""criar coluna descricao e alterar nome para name

Revision ID: e724c0559d33
Revises: ad945753db98
Create Date: 2016-02-02 15:09:05.961000

"""

# revision identifiers, used by Alembic.
revision = 'e724c0559d33'
down_revision = 'ad945753db98'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('ALTER TABLE perfil RENAME COLUMN descricao TO name')
    op.add_column('perfil', sa.Column('description', sa.VARCHAR(100)))


def downgrade():
    op.execute('ALTER TABLE perfil RENAME COLUMN name TO descricao')
    op.drop_column('perfil', 'description')

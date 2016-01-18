"""criar tabela nucleos

Revision ID: 42660024c5f9
Revises: 
Create Date: 2016-01-18 08:02:39.438000

"""

# revision identifiers, used by Alembic.
revision = '42660024c5f9'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
    'nucleo',
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('descricao', sa.VARCHAR(100), nullable=False),
    sa.Column('objetivo', sa.VARCHAR(300)),
    )


def downgrade():
    op.drop_table(
        'nucleo')

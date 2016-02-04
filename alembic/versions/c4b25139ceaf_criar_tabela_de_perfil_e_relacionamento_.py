"""criar tabela de perfil e relacionamento com agente'

Revision ID: c4b25139ceaf
Revises: c261947b6380
Create Date: 2016-02-02 12:15:44.301000

"""

# revision identifiers, used by Alembic.
revision = 'c4b25139ceaf'
down_revision = 'c261947b6380'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'perfil',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('descricao', sa.VARCHAR(35), nullable=False),
    )
    
    op.add_column('agente', sa.Column('id_perfil', sa.Integer, sa.ForeignKey('perfil.id')))


def downgrade():
    op.execute('ALTER TABLE agente DROP COLUMN id_perfil')
    op.drop_table('perfil')

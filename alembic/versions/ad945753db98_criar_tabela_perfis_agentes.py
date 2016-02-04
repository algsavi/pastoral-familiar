"""criar tabela perfis_agentes

Revision ID: ad945753db98
Revises: c4b25139ceaf
Create Date: 2016-02-02 14:21:36.309000

"""

# revision identifiers, used by Alembic.
revision = 'ad945753db98'
down_revision = 'c4b25139ceaf'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'perfis_agentes',
        sa.Column('id_agente', sa.Integer, sa.ForeignKey('agente.id')),
        sa.Column('id_perfil', sa.Integer, sa.ForeignKey('perfil.id'))
    )

    op.execute('ALTER TABLE agente DROP COLUMN id_perfil')



def downgrade():
    op.drop_table('perfis_agentes')
    op.add_column('agente', sa.Column('id_perfil', sa.Integer, sa.ForeignKey('perfil.id')))
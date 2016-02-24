"""criar tabela casal encontrista

Revision ID: e39357dd841f
Revises: 7f2e5ad7b3bd
Create Date: 2016-02-19 09:40:52.219000

"""

# revision identifiers, used by Alembic.
revision = 'e39357dd841f'
down_revision = '7f2e5ad7b3bd'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'encontrista',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.VARCHAR(65), nullable=False),
        sa.Column('dt_nascimento', sa.Date(), nullable=False),
        sa.Column('email', sa.VARCHAR(40), nullable=False),
        sa.Column('celular', sa.VARCHAR(15), nullable=False),
        sa.Column('sexo', sa.VARCHAR(1), nullable=False)
    )

    op.create_table(
        'casal_encontrista',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('rua', sa.VARCHAR(65), nullable=False),
        sa.Column('cep', sa.VARCHAR(10), nullable=False),
        sa.Column('numero', sa.Integer(), nullable=False),
        sa.Column('complemento', sa.VARCHAR(10), nullable=False),
        sa.Column('cidade', sa.VARCHAR(30), nullable=False),
        sa.Column('bairro', sa.VARCHAR(30), nullable=False),
        sa.Column('uf', sa.VARCHAR(2), nullable=False),
        sa.Column('telefone_residencial', sa.VARCHAR(15)),
        sa.Column('id_encontro', sa.Integer, sa.ForeignKey('evento.id')),
        sa.Column('id_esposa', sa.Integer, sa.ForeignKey('encontrista.id')),
        sa.Column('id_esposo', sa.Integer, sa.ForeignKey('encontrista.id')),
    )


def downgrade():
    op.drop_table('casal_encontrista')
    op.drop_table('encontrista')

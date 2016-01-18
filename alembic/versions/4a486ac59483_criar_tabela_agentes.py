"""criar tabela agentes

Revision ID: 4a486ac59483
Revises: 42660024c5f9
Create Date: 2016-01-18 09:47:35.031000

"""

# revision identifiers, used by Alembic.
revision = '4a486ac59483'
down_revision = '42660024c5f9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'agente',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.VARCHAR(35), nullable=False),
        sa.Column('dt_nascimento', sa.Date(), nullable=False),
        sa.Column('email', sa.VARCHAR(40), nullable=False, unique=True),
        sa.Column('celular', sa.VARCHAR(15), nullable=False),
        sa.Column('endereco', sa.VARCHAR(65), nullable=False),
        sa.Column('cidade', sa.VARCHAR(30), nullable=False),
        sa.Column('bairro', sa.VARCHAR(30), nullable=False),
        sa.Column('telefone_residencial', sa.VARCHAR(15)),
        sa.Column('senha', sa.VARCHAR(250)),
        sa.Column('id_nucleo', sa.Integer, sa.ForeignKey('nucleo.id'))
    )


def downgrade():
    op.drop_table(
        'agente')

"""Store user agent string with files

Revision ID: dd0766afb7d2
Revises: 30bfe33aa328
Create Date: 2023-03-29 07:18:49.113200

"""

# revision identifiers, used by Alembic.
revision = 'dd0766afb7d2'
down_revision = '30bfe33aa328'

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ua', sa.UnicodeText(), nullable=True))


def downgrade():
    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.drop_column('ua')

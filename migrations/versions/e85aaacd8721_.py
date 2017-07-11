"""empty message

Revision ID: e85aaacd8721
Revises: 9e1204b2e096
Create Date: 2017-07-10 20:33:41.743320

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'e85aaacd8721'
down_revision = '9e1204b2e096'

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('discount_code_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'events', 'discount_codes', ['discount_code_id'], ['id'], ondelete='CASCADE')
    op.add_column('events_version', sa.Column('discount_code_id', sa.Integer(), autoincrement=False, nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'discount_code_id')
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'discount_code_id')
    ### end Alembic commands ###
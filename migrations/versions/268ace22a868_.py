"""empty message

Revision ID: 268ace22a868
Revises: 9a7a4b5bb700
Create Date: 2023-08-28 19:24:07.496614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '268ace22a868'
down_revision = '9a7a4b5bb700'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rating', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('rating_user_id_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rating', schema=None) as batch_op:
        batch_op.create_unique_constraint('rating_user_id_key', ['user_id'])
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###

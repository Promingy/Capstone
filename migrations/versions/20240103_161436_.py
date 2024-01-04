"""empty message

Revision ID: 7c0371185503
Revises: 
Create Date: 2024-01-03 16:14:36.727353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c0371185503'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('measurements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('measurement_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('bio', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('profile_pic', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=75), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('servings', sa.Integer(), nullable=False),
    sa.Column('prep_time', sa.Integer(), nullable=False),
    sa.Column('cook_time', sa.Integer(), nullable=False),
    sa.Column('preview_image', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'recipe_id')
    )
    op.create_table('quantities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('ingredient_measurement_id', sa.Integer(), nullable=True),
    sa.Column('ingredient', sa.String(), nullable=False),
    sa.Column('ingredient_quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_measurement_id'], ['measurements.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('edited', sa.Boolean(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savedrecipes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'recipe_id')
    )
    op.create_table('steps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('step_number', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('steps')
    op.drop_table('savedrecipes')
    op.drop_table('reviews')
    op.drop_table('quantities')
    op.drop_table('likes')
    op.drop_table('recipes')
    op.drop_table('users')
    op.drop_table('measurements')
    op.drop_table('categories')
    # ### end Alembic commands ###

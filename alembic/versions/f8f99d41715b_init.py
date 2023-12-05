"""init

Revision ID: f8f99d41715b
Revises: 
Create Date: 2023-12-05 11:19:45.181735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from datamodel import Car_Type, Engine_Type


# revision identifiers, used by Alembic.
revision: str = 'f8f99d41715b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    car_type_enum = postgresql.ENUM('sedan', 'suv', 'sport', name='car_types')
    car_type_enum.create(op.get_bind(), checkfirst=False)
    engine_type_enum = postgresql.ENUM('fuel', 'electric', name='engine_types')
    engine_type_enum.create(op.get_bind(), checkfirst=False)

    op.create_table(
        'cars',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('car_name', sa.String, nullable=False),
        sa.Column('price', sa.Integer, nullable=False),
        sa.Column('year', sa.String, nullable=False),
        sa.Column('car_type', car_type_enum, nullable=False),
        sa.Column('engine_type', engine_type_enum, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('cars'),
    sa.Enum('sedan', 'suv', 'sport', name='car_types').drop(op.get_bind()),
    sa.Enum('fuel', 'electric', name='engine_types').drop(op.get_bind())

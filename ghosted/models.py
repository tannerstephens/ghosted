from .extensions import db

class Spectre(db.Model):
  id = db.Column(db.Integer, primary_key=True)

  ghost_id = db.Column(db.String(8), unique=True)
  is_active = db.Column(db.Boolean, default=False)
  is_root = db.Column(db.Boolean, default=False)

  haunt_id = db.Column(db.Integer, db.ForeignKey("haunt.id"))
  parent_id = db.Column(db.Integer, db.ForeignKey("spectre.id"))

  children = db.relationship("Spectre", backref=db.backref('parent', remote_side=[id]))

  def as_dict(self):
    active_children = filter(lambda child : child.is_active, self.children)
    children = list(map(lambda child : { 'id' : child.id, 'is_active' : child.is_active }, active_children))

    return dict(
      id = self.id,
      is_active = self.is_active,
      is_root = self.is_root,
      children = children,
      ghost_id = self.ghost_id
    )


class Haunt(db.Model):
  id = db.Column(db.Integer, primary_key=True)

  spectres = db.relationship("Spectre", backref=db.backref('haunt', remote_side=[id]))

from django.conf import settings


def category(self):
    from leonardo.module.web.widget.application.reverse import app_reverse

    if self.pk == settings.ST_TOPIC_PRIVATE_CATEGORY_PK:
        return app_reverse(
            'topic:private:index',
            'leonardo_spirit.apps.spirit')

    else:
        return app_reverse(
            'category:detail',
            'leonardo_spirit.apps.spirit',
            kwargs={'pk': str(self.id), 'slug': self.slug})


def topic(self):
    from leonardo.module.web.widget.application.reverse import app_reverse

    if self.category_id == settings.ST_TOPIC_PRIVATE_CATEGORY_PK:
        return app_reverse(
            'topic:private:detail',
            'leonardo_spirit.apps.spirit',
            kwargs={'topic_id': str(self.id), 'slug': self.slug})

    else:
        return app_reverse(
            'topic:detail',
            'leonardo_spirit.apps.spirit',
            kwargs={'pk': str(self.id), 'slug': self.slug})


def userprofile(self):
    from leonardo.module.web.widget.application.reverse import app_reverse

    return app_reverse(
        'user:detail',
        'leonardo_spirit.apps.spirit',
        kwargs={'pk': self.user.pk, 'slug': self.slug})


def comment(self):
    from leonardo.module.web.widget.application.reverse import app_reverse

    return app_reverse(
        'comment:find',
        'leonardo_spirit.apps.spirit',
        kwargs={'pk': str(self.id)})

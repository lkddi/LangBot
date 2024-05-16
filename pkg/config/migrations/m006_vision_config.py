from __future__ import annotations

from .. import migration


@migration.migration_class("vision-config", 6)
class VisionConfigMigration(migration.Migration):
    """迁移"""

    async def need_migrate(self) -> bool:
        """判断当前环境是否需要运行此迁移"""
        return "enable-vision" not in self.ap.provider_cfg.data

    async def run(self):
        """执行迁移"""
        if "enable-vision" not in self.ap.provider_cfg.data:
            self.ap.provider_cfg.data["enable-vision"] = False

        await self.ap.provider_cfg.dump_config()

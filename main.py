import click
from note_manager import NoteManager
from search_engine import SearchEngine

@click.group()
def cli():
    """Local AI Note CLI - 基于AI的本地笔记管理工具"""
    pass

@cli.command()
def version():
    """显示版本信息"""
    click.echo("Local AI Note CLI v0.1.0")

@cli.command()
@click.argument("content")
@click.option("--tags", "-t", multiple=True, help="笔记标签")
def add(content, tags):
    """添加新笔记"""
    nm = NoteManager()
    se = SearchEngine()
    note_id = nm.add_note(content, list(tags))
    se.add_note_to_index(note_id, content)
    click.echo(f"✅ 笔记已添加，ID: {note_id}")

@cli.command()
@click.argument("note_id", type=int)
def delete(note_id):
    """删除指定ID的笔记"""
    nm = NoteManager()
    if nm.delete_note(note_id):
        click.echo(f"✅ 笔记 {note_id} 已删除")
    else:
        click.echo(f"❌ 笔记 {note_id} 不存在")

@cli.command()
def list():
    """列出所有笔记"""
    nm = NoteManager()
    notes = nm.list_notes()
    if not notes:
        click.echo("暂无笔记")
        return
    for note in notes:
        tags_str = f" [{' '.join(note['tags'])}]" if note['tags'] else ""
        click.echo(f"[{note['id']}] {note['content'][:60]}...{tags_str}")

@cli.command()
@click.argument("query")
def search(query):
    """语义搜索笔记"""
    se = SearchEngine()
    results = se.search_notes(query)
    if not results:
        click.echo("未找到相关笔记")
        return
    click.echo(f"找到 {len(results)} 条相关笔记：")
    for res in results:
        click.echo(f"\n[{res['note']['id']}] {res['note']['content']}")

if __name__ == "__main__":
    cli()
